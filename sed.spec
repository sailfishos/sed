%define _bindir /bin

Name:       sed
Summary:    A GNU stream text editor
Version:    4.1.5
Release:    2
Epoch:      1
Group:      Applications/Text
License:    GPLv2+
URL:        http://sed.sourceforge.net/
Source0:    ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.gz
Patch0:     sed-aarch64.patch
BuildRequires:  glibc-devel

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure --disable-static \
    --without-included-regex

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang %{name}

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        AUTHORS BUGS ChangeLog README THANKS

%lang_package

%check
make check

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/sed

%files doc
%defattr(-,root,root,-)
%license COPYING.DOC
%{_infodir}/%{name}.*
%{_mandir}/man1/%{name}.*
%{_docdir}/%{name}-%{version}
