# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate sys-info

Name:           rust-%{crate}
Version:        0.5.6
Release:        2%{?dist}
Summary:        Get system information in Rust

License:        MIT
URL:            https://crates.io/crates/sys-info
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(libc) >= 0.2.29 with crate(libc) < 0.3.0)
# [build-dependencies]
BuildRequires:  (crate(cc) >= 1.0.0 with crate(cc) < 2.0.0)
BuildRequires:  %{_bindir}/hostname

%description
%{summary}.

%package        devel
Summary:        %{summary}
Requires:       %{_bindir}/hostname
BuildArch:      noarch

%description    devel
Get system information in Rust.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# https://github.com/FillZpp/sys-info-rs/issues/25
%cargo_test \
  %ifarch ppc64 ppc64le
    || :
  %else
    ;
  %endif
%endif

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.6-1
- Update to 0.5.6

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.5-2
- Rebuild for rust-packaging v5

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.5-1
- Update to 0.5.5

* Mon Jan 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-1
- Update to 0.5.4

* Mon Dec 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.3-1
- Initial package
