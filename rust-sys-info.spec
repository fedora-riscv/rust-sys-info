# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate sys-info

Name:           rust-sys-info
Version:        0.9.1
Release:        %autorelease.rv64
Summary:        Get system information in Rust

License:        MIT
URL:            https://crates.io/crates/sys-info
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Get system information in Rust. For now it supports Linux, Mac OS X,
illumos, Solaris, FreeBSD, OpenBSD, and Windows.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%if %{with check}
%check
%ifnarch riscv64
%cargo_test
%endif
%endif

%install
%cargo_install

%changelog
%autochangelog
