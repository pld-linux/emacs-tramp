# NOTE: tramp 2.3.4 is already in emacs 26.2
Summary:	Transparent Remote Access for Emacs
Summary(pl.UTF-8):	Przezroczysty zdalny dostęp do plików dla Emacsa
Name:		emacs-tramp
Version:	2.5.1
Release:	0.1
License:	GPL v3+
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/tramp/tramp-%{version}.tar.gz
# Source0-md5:	d98b79d4d7d6f659e869866207e3b237
Patch0:		tramp-info.patch
URL:		http://www.gnu.org/software/tramp/
BuildRequires:	emacs >= 25.1
BuildRequires:	texinfo >= 4.6
Requires:	emacs >= 25.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tramp stands for `Transparent Remote (file) Access, Multiple
Protocol'. This package provides remote file editing, similar to
Ange-FTP.

The difference is that Ange-FTP uses FTP to transfer files between the
local and the remote host, whereas Tramp uses a combination of `rsh'
and `rcp' or other work-alike programs, such as `ssh'/`scp'.

%description -l pl.UTF-8
Tramp oznacza "Transparent Remote (file) Access, Multiple Protocol",
czyli przezroczysty zdalny dostęp do plików przy użyciu wielu
protokołów. Pakiet pozwala na edycję plików zdalnych, podobnie do
Ange-FTP.

Różnica jest taka, że Ange-FTP używa FTP do przesyłania plików między
komputerem lokalnym i zdalnym, a Trump używa kombinacji "rsh" i "rcp"
albo podobnie działających programów, takich jak "ssh"/"scp".

%prep
%setup -q -n tramp-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_infodir}/tramp{,.info}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog README THANKS TODO
%{_emacs_lispdir}/tramp*.el
%{_emacs_lispdir}/tramp*.elc
%{_infodir}/tramp.info*
