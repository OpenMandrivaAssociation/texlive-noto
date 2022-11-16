Name:		texlive-noto
Version:	64351
Release:	1
Summary:	Support for Noto fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/noto
License:	lppl ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noto.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noto.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the NotoSerif, NotoSans and NotoSansMono families
of fonts, designed by Steve Matteson for Google.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/noto
%{_texmfdistdir}/fonts/vf/google/noto
%{_texmfdistdir}/fonts/type1/google/noto
%{_texmfdistdir}/fonts/truetype/google/noto
%{_texmfdistdir}/fonts/tfm/google/noto
%{_texmfdistdir}/fonts/map/dvips/noto
%{_texmfdistdir}/fonts/enc/dvips/noto
%doc %{_texmfdistdir}/doc/fonts/noto

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
