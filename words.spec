Summary:	English dictionary for /usr/share/dict
Summary(de):	Englisches Wörterbuch für /usr/share/dict
Summary(fr):	Dictionnaire anglais pour /etc/share/dict
Summary(pl):	S³ownik angielski dla /usr/share/dict
Summary(tr):	ngilizce sözlük
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
Dieses Paket enthält das englische Wörterbuch in /usr/share/dict. Es
wird von Programmen wie ispell als Wortdatenbank, z.B. zum Prüfen der
Rechtschreibung, verwendet.

%description -l fr
Ce paquetage contient le dictionnaire anglais dans /usr/share/dict. Il
est utilisé par des programmes comme ispell comme base de données de
mots pour vérifier l'orthographe.

%description -l pl
W pakiecie tym znajduje siê s³ownik angielski. U¿ywany jest przez
programy takie jak ispell, kpasswd itp.

%description -l tr
Bu paket ingilizce sözlük içermektedir. Ispell gibi yazýlýmlar bu
sözcük veri tabanýný kullanarak yazým hatalarýný bulmaya çalýþýrlar.

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
