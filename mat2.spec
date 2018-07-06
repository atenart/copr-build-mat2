Name:		mat2
Version:	0.1.3
Release:	1%{?dist}
Summary:	Mat2 removes metadata from common file types.

License:	GPLv3+
URL:		https://0xacab.org/jvoisin/mat2
Source0:	https://0xacab.org/jvoisin/mat2/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	python3-devel
BuildArch:	noarch

Requires:	python3
Requires:	python3-gobject
Requires:	python3-mutagen
Requires:	python3-cairo
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

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/%{name}

%changelog
* Tue Jul 06 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.1.3-1
- Bump to 0.1.3.
- See https://0xacab.org/jvoisin/mat2/tags/0.1.3
- See https://0xacab.org/jvoisin/mat2/tags/0.1.2
* Tue Jun 12 2018 Antoine Tenart <antoine.tenart@ack.tf> - 0.1.1-1
- First mat2 package.
