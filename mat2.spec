Name:		mat2
Version:	0.12.1
Release:	1%{?dist}
Summary:	Mat2 removes metadata from common file types.

License:	GPLv3+
URL:		https://0xacab.org/jvoisin/mat2
Source0:	https://0xacab.org/jvoisin/mat2/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://0xacab.org/jvoisin/mat2/uploads/0f5c82d07da3f01ce78f8a3bf8c2a1b6/mat2-0.12.1.tar.gz.asc
Source2:	gpgkey-9FCDEE9E1A381F311EA62A7404D041E8171901CC.gpg

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	gnupg2

# %check dependencies
BuildRequires:	python3
BuildRequires:	python3-gobject
BuildRequires:	python3-mutagen
BuildRequires:	python3-cairo
BuildRequires:	bubblewrap
BuildRequires:	cairo-gobject
BuildRequires:	poppler-glib
BuildRequires:	gdk-pixbuf2-modules
BuildRequires:	perl-Image-ExifTool
BuildRequires:	mailcap

Requires:	python3
Requires:	python3-gobject
Requires:	python3-mutagen
Requires:	python3-cairo
Requires:	bubblewrap
Requires:	cairo-gobject
Requires:	poppler-glib
Requires:	gdk-pixbuf2-modules
Requires:	perl-Image-ExifTool
Requires:	mailcap

%description
Metadata consist of information that characterizes data.
Metadata are used to provide documentation for data products.
In essence, metadata answer who, what, when, where, why, and how about
every facet of the data that are being documented.

Metadata within a file can tell a lot about you.
Cameras record data about when a picture was taken and what
camera was used. Office documents like PDF or Office automatically adds
author and company information to documents and spreadsheets.
Maybe you don't want to disclose those information on the web.

This is precisely the job of MAT2: getting rid, as much as possible, of
metadata.

%package -n mat2-nautilus
Summary: Mat2 Nautilus extension
Requires: mat2
Requires: nautilus
Requires: python3-nautilus

%description -n mat2-nautilus
Mat2 Nautilus extension to allow removing metadata using Mat2 using a
dedicated menu item.

%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%py3_build

%install
%py3_install
install -m 0644 -D nautilus/mat2.py %{buildroot}/usr/share/nautilus-python/extensions/mat2.py
install -m 0644 -D doc/mat2.1 %{buildroot}%{_mandir}/man1/mat2.1

#%check
#%{__python3} -m unittest discover

%files
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_mandir}/man1/mat2.1*
%license LICENSE
%doc README.md doc/*

%files -n mat2-nautilus
/usr/share/nautilus-python/extensions/mat2.py
%license LICENSE
%doc nautilus/README.md

%changelog
* Mon Mar 22 2021 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.1-1
- Bump to 0.12.1.
- See https://0xacab.org/jvoisin/mat2/-/releases/0.12.1

* Sat Dec 19 2020 Antoine Tenart <antoine.tenart@ack.tf> - 0.12.0-1
- Bump to 0.12.0.
- See https://0xacab.org/jvoisin/mat2/-/blob/master/CHANGELOG.md#0120-2020-12-18

* Sun Mar 29 2020 Antoine Tenart <antoine.tenart@ack.tf> - 0.11.0-1
- Bump to 0.11.0.
- See https://0xacab.org/jvoisin/mat2/-/blob/master/CHANGELOG.md#0110-2020-03-29

* Mon Feb 10 2020 Antoine Tenart <antoine.tenart@ack.tf> - 0.10.1-1
- Bump to 0.10.1.
- See https://0xacab.org/jvoisin/mat2/tags/0.10.1

* Mon Dec 02 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.10.0-1
- Bump to 0.10.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.10.0

* Sat May 11 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.9.0-1
- Bump to 0.9.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.9.0

* Wed Apr 24 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.8.0-3
- Enable tarball verification.
- Add build time checks.

* Wed Mar 27 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.8.0-2
- Install mat2's man page and docs.
- Stop listing ffmpeg as a mandatory dependency.

* Fri Mar 22 2019 Antoine Tenart <antoine.tenart@ack.tf> - 0.8.0-1
- Bump to 0.8.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.8.0
- See https://0xacab.org/jvoisin/mat2/tags/0.7.0

* Sat Nov 10 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.6.0-1
- Bump to 0.6.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.6.0

* Wed Oct 24 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.5.0-1
- Bump to 0.5.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.5.0

* Thu Oct 11 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.4.0-1
- Bump to 0.4.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.4.0

* Sat Sep 01 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.3.1-1
- Bump to 0.3.1.
- See https://0xacab.org/jvoisin/mat2/tags/0.3.1

* Thu Aug 23 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.3.0-1
- Bump to 0.3.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.3.0

* Wed Jul 11 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.2.0-1
- Bump to 0.2.0.
- See https://0xacab.org/jvoisin/mat2/tags/0.2.0

* Fri Jul 06 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.1.3-1
- Bump to 0.1.3.
- See https://0xacab.org/jvoisin/mat2/tags/0.1.3
- See https://0xacab.org/jvoisin/mat2/tags/0.1.2

* Tue Jun 12 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.1.1-1
- First mat2 package.
