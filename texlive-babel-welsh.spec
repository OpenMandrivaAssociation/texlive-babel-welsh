# revision 30299
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/welsh
# catalog-date 2013-05-03 01:23:11 +0200
# catalog-license lppl1.3
# catalog-version 1.0d
Name:		texlive-babel-welsh
Version:	1.0d
Release:	9
Summary:	babel-welshBabel support for Welsh
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/welsh
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-welsh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-welsh.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-welsh.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the language definition file for Welsh.
(Mostly Welsh-language versions of the standard names in a
LaTeX file.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-welsh/welsh.ldf
%doc %{_texmfdistdir}/doc/generic/babel-welsh/welsh.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-welsh/welsh.dtx
%doc %{_texmfdistdir}/source/generic/babel-welsh/welsh.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
