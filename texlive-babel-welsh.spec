%global tl_name babel-welsh
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1c
Release:	%{tl_revision}.1
Summary:	Babel support for Welsh
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/welsh
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-welsh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-welsh.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-welsh.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for Welsh. (Mostly
Welsh-language versions of the standard names in a LaTeX file.)

