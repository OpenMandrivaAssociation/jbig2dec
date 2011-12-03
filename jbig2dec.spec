%define	major 0
%define libname %mklibname jbig2dec %{major}
%define develname %mklibname jbig2dec -d

Summary:	A decoder implementation of the JBIG2 image compression format
Name:		jbig2dec
Version:	0.11
Release:	3
License:	GPLv2
Group:		Graphics
URL:		http://jbig2dec.sourceforge.net/
Source0:	http://ghostscript.com/~giles/jbig2/jbig2dec/%{name}-%{version}.tar.gz
Patch1:		jbig2dec-0.10-jbig2dec-nullderef.diff
BuildRequires:	autoconf automake libtool

%description
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit 
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

%package -n	%{libname}
Summary:	A decoder implementation of the JBIG2 image compression format
Group:          System/Libraries

%description -n	%{libname}
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit 
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package provides the shared jbig2dec library.

%package -n	%{develname}
Summary:	Static library and header files for development with jbig2dec
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	jbig2dec-devel = %{version}-%{release}

%description -n	%{develname}
jbig2dec is a decoder implementation of the JBIG2 image compression format.
JBIG2 is designed for lossy or lossless encoding of 'bilevel' (1-bit 
monochrome) images at moderately high resolution, and in particular scanned
paper documents. In this domain it is very efficient, offering compression
ratios on the order of 100:1.

This package is only needed if you plan to develop or compile applications
which requires the jbig2dec library.

%prep

%setup -q
%patch1 -p0

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

%build
libtoolize --copy --force; aclocal; autoheader; autoconf; automake --foreign --copy --add-missing

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files
%attr(0755,root,root) %{_bindir}/jbig2dec
%attr(0644,root,root) %{_mandir}/man1/jbig2dec.1*

%files -n %{libname}
%doc CHANGES COPYING LICENSE README
%attr(0755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{develname}
%attr(0644,root,root) %{_includedir}/*.h
%attr(0644,root,root) %{_libdir}/*.so
