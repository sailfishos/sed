%define _bindir /bin

Name:       gnu-sed
Summary:    A GNU stream text editor
Version:    4.1.5+git1
Release:    0
License:    GPLv2+
URL:        http://sed.sourceforge.net/
Source0:    sed-4.1.5.tar.gz
Patch0:     sed-aarch64.patch
BuildRequires:  glibc-devel
Provides:   sed = 1:4.1.5+git1
Obsoletes:  sed < 1:4.1.5+git1

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
Provides:  sed-docs = 1:4.1.5+git1
Obsoletes: sed-docs < 1:4.1.5+git1

%description doc
Man and info pages for %{name}.

%package locale
Summary: Translations and Locale for package %{name}

%description locale
This package provides translations for package %{name}.

%prep
%autosetup -p1 -n sed-4.1.5

%build
%configure --disable-static \
    --without-included-regex

%make_build

%install
rm -rf %{buildroot}
%make_install

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang sed

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        AUTHORS BUGS ChangeLog README THANKS

%files locale -f sed.lang
%defattr(-,root,root,-)

%check
make check

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/sed

%files doc
%defattr(-,root,root,-)
%license COPYING.DOC
%{_infodir}/sed.*
%{_mandir}/man1/sed.*
%{_docdir}/%{name}-%{version}
