%define	major	0
%define libname %mklibname jbig2dec %{major}
%define devname %mklibname jbig2dec -d

Summary:	A decoder implementation of the JBIG2 image compression format
Name:		jbig2dec
Version:	0.17
Release:	1
License:	GPLv2
Group:		Graphics
Url:		http://jbig2dec.com/
Source0:	https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs950/jbig2dec-%{version}.tar.gz
Patch0:		jbig2dec-automake-1.13.patch
BuildRequires:	libtool

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit 
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

%package -n	%{libname}
Summary:	A decoder implementation of the JBIG2 image compression format
Group:		System/Libraries

%description -n	%{libname}
This package provides the shared jbig2dec library.

%package -n	%{devname}
Summary:	Static library and header files for development with jbig2dec
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package is only needed if you plan to develop or compile applications
which requires the jbig2dec library.

%prep
%setup -q
%autopatch -p1
autoreconf -fi

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc CHANGES COPYING LICENSE README
%{_bindir}/jbig2dec
%{_mandir}/man1/jbig2dec.1*

%files -n %{libname}
%{_libdir}/libjbig2dec.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
