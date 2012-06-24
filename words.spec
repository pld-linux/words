Summary:	English dictionary for /usr/share/dict
Summary(de):	Englisches W�rterbuch f�r /usr/share/dict
Summary(fr):	Dictionnaire anglais pour /etc/share/dict
Summary(pl):	S�ownik angielski dla /usr/share/dict
Summary(tr):	ngilizce s�zl�k
Name:		words
Version:	2
Release:	19
License:	Freeware
Group:		Applications/Text
Source0:	ftp://sunsite.unc.edu/pub/Linux/libs/linux.%{name}.%{version}.tar.gz
# Source0-md5:	e07b5955c35923cfad105b05666342f1
Patch0:		linux.%{name}-jbj.patch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the English dictionary in /usr/share/dict. It is
used by programs like ispell as a database of words to check for
spelling and so forth.

%description -l de
Dieses Paket enth�lt das englische W�rterbuch in /usr/share/dict. Es
wird von Programmen wie ispell als Wortdatenbank, z.B. zum Pr�fen der
Rechtschreibung, verwendet.

%description -l fr
Ce paquetage contient le dictionnaire anglais dans /usr/share/dict. Il
est utilis� par des programmes comme ispell comme base de donn�es de
mots pour v�rifier l'orthographe.

%description -l pl
W pakiecie tym znajduje si� s�ownik angielski. U�ywany jest przez
programy takie jak ispell, kpasswd itp.

%description -l tr
Bu paket ingilizce s�zl�k i�ermektedir. Ispell gibi yaz�l�mlar bu
s�zc�k veri taban�n� kullanarak yaz�m hatalar�n� bulmaya �al���rlar.

%prep
%setup -q -c
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dict

install usr/dict/linux.words $RPM_BUILD_ROOT%{_datadir}/dict/american-english
ln -sf american-english $RPM_BUILD_ROOT%{_datadir}/dict/words

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc usr/dict/{README.linux.words*,README2.linux.words*}
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/dict/*
