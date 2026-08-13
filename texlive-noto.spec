%global tl_name noto
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for Noto fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/noto
License:	lppl ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noto.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noto.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the NotoSerif, NotoSans and NotoSansMono families of fonts, designed by
Steve Matteson for Google.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from noto:
Map noto.map
TL_DROPIN_EOF
