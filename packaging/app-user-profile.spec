
Name: app-user-profile
Epoch: 1
Version: 1.6.0
Release: 1%{dist}
Summary: User Profile
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-accounts
Requires: app-groups
Requires: app-users

%description
The User Profile app is used to change your password and, depending on your system settings, update other profile settings.

%package core
Summary: User Profile - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-accounts-core
Requires: app-groups-core
Requires: app-users-core >= 1.0.6

%description core
The User Profile app is used to change your password and, depending on your system settings, update other profile settings.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/user_profile
cp -r * %{buildroot}/usr/clearos/apps/user_profile/

install -D -m 0644 packaging/user_profile.acl %{buildroot}/var/clearos/base/access_control/authenticated/user_profile

%post
logger -p local6.notice -t installer 'app-user-profile - installing'

%post core
logger -p local6.notice -t installer 'app-user-profile-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/user_profile/deploy/install ] && /usr/clearos/apps/user_profile/deploy/install
fi

[ -x /usr/clearos/apps/user_profile/deploy/upgrade ] && /usr/clearos/apps/user_profile/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-user-profile - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-user-profile-core - uninstalling'
    [ -x /usr/clearos/apps/user_profile/deploy/uninstall ] && /usr/clearos/apps/user_profile/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/user_profile/controllers
/usr/clearos/apps/user_profile/htdocs
/usr/clearos/apps/user_profile/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/user_profile/packaging
%dir /usr/clearos/apps/user_profile
/usr/clearos/apps/user_profile/deploy
/usr/clearos/apps/user_profile/language
/var/clearos/base/access_control/authenticated/user_profile
