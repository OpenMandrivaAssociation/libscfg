%define api 1

%define libname %mklibname scfg
%define devname %mklibname -d scfg

Name:           libscfg
Version:        0.1.1
Release:        1
Summary:        C library for a simple configuration file format
Group:          System/Library
License:        MIT
URL:            https://sr.ht/~emersion/libscfg/
Source0:        https://git.sr.ht/~emersion/libscfg/refs/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:          https://sr.ht/~emersion/libscfg/commit/3bdba8c2.patch#/libscfg-0.1.1-build-set-library-version-and-soversion.patch

BuildRequires:  gnupg2
BuildRequires:  meson

%description
C library for a simple configuration file format

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libscfg.so.%{api}
%{_libdir}/libscfg.so.%{version}

%files -n %{devname}
%{_includedir}/scfg.h
%{_libdir}/libscfg.so
%{_libdir}/pkgconfig/scfg.pc
