%define _unpackaged_files_terminate_build 1

Name: align-rs
Version: 1.0.1
Release: alt1.gitc268c1f
Summary: align a command line utility for aligning text.
License: MIT / Apache v2
Group: Development/Other
Url: https://github.com/KhalilOuali/align-rs
Source: %name-%version.tar

BuildRequires(pre):  rust rust-cargo

%description
Aligns text within the terminal (or a specified number of columns).
The text is treated as a block, and you can align the content within it, or align it within the space.

%prep
%setup

%build
cargo build --release

%install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/%name %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Mon Aug 21 2023 Anton Protopopov <antpro@altlinux.org> 1.0.1-alt1.gitc268c1f
- Initial package


