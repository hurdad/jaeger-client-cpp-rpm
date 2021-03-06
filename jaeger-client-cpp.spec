Name:           jaeger-client-cpp
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Jaeger SDK with OpenTracing API for C++ binding
Group:          System Environment/Libraries
License:	Apache 2.0
URL:            https://github.com/jaegertracing/jaeger-client-cpp
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:  thrift-devel
BuildRequires:	opentracing-cpp-devel

%description
Jaeger SDK with OpenTracing API for C++ binding
%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	thrift-devel
Requires:	opentracing-cpp-devel

%description devel
Development files for %{name}.

%prep
%setup

%build
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DHUNTER_ENABLED=OFF -DBUILD_TESTING=OFF -DJAEGERTRACING_WITH_YAML_CPP=OFF -DJAEGERTRACING_BUILD_EXAMPLES=OFF

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md 
%{_libdir}/libjaegertracing.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/libjaegertracing.a
%{_includedir}/jaegertracing
%{_libdir}/cmake/jaegertracing/*.cmake

%changelog
