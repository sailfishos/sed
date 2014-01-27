# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
%define _bindir /bin
# << macros

Name:       sed
Summary:    A GNU stream text editor
Version:    4.1.5
Release:    1
Epoch:      1
Group:      Applications/Text
License:    GPLv2+
URL:        http://sed.sourceforge.net/
Source0:    ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.gz
Source100:  sed.yaml
Patch0:     sed-aarch64.patch
BuildRequires:  glibc-devel


%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.




%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --without-included-regex

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%find_lang %{name}

%docs_package

%lang_package
# << install post
%check
# >> check
make check
# << check






%files
%defattr(-,root,root,-)
# >> files
%doc COPYING COPYING.DOC
%{_bindir}/sed
# << files


