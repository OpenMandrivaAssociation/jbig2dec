# jbig2dec is used by ghostscript, ghostscript is used by libspectre,
# libspectre is used by cairo, cairo is used by gtk-3.0, gtk-3.0
# is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define	major	0
%define libname %mklibname jbig2dec %{major}
%define devname %mklibname jbig2dec -d
%define lib32name %mklib32name jbig2dec %{major}
%define dev32name %mklib32name jbig2dec -d

Summary:	A decoder implementation of the JBIG2 image compression format
Name:		jbig2dec
Version:	0.19
Release:	2
License:	GPLv2
Group:		Graphics
Url:		http://jbig2dec.com/
Source0:	https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs9530/jbig2dec-%{version}.tar.gz
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

%if %{with compat32}
%package -n	%{lib32name}
Summary:	A decoder implementation of the JBIG2 image compression format (32-bit)
Group:		System/Libraries

%description -n	%{lib32name}
This package provides the shared jbig2dec library.

%package -n	%{dev32name}
Summary:	Static library and header files for development with jbig2dec (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}
Requires:	%{lib32name} = %{version}

%description -n	%{dev32name}
This package is only needed if you plan to develop or compile applications
which requires the jbig2dec library.
%endif

%prep
%setup -q
%autopatch -p1
autoreconf -fi

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure


%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libjbig2dec.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
