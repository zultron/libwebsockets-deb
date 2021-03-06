%global git_rev 95a8abb

Name:       libwebsockets
VCS:        profile/ivi/libwebsockets#daeb4e88c69e07eef94586ed8a68f891a16f94c5
Summary:    WebSocket Library
Version:    1.22
Release:    0.1.git%{git_rev}%{?dist}
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://git.warmcat.com/cgi-bin/cgit/libwebsockets/
Source0:    %{url}/snapshot/%{name}-%{git_rev}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: cmake
BuildRequires: g++

%description
C Websockets Server Library

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files needed for building websocket clients and servers

%prep
%setup -q -n %{name}-%{git_rev}

%build

%cmake -DWITH_SSL=On

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
if test %{_libdir} != %{_prefix}/lib; then
    # Fix install path of cmake helpers
    mkdir -p %{buildroot}/%{_libdir}/cmake
    mv %{buildroot}/%{_prefix}/lib/cmake/libwebsockets \
	%{buildroot}/%{_libdir}/cmake
fi

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/libwebsockets*
%{_libdir}/libwebsockets*.so.*
%{_datadir}/libwebsockets-test-server/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libwebsockets.h
%{_libdir}/libwebsockets.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/libwebsockets
%{_libdir}/libwebsockets.a


%changelog
* Thu Jan 22 2015 John Morris <john@zultron.com> - 1.22-0.1.git95a8abb
- Packaging from Tizen OBS
- Update to git rev 95a8abb for Fedora and Machinekit deps

* Tue Jun 18 2013 @25cd862
- sumbitting to tizen
* Mon Jun  3 2013 @8a05fa0
- Switching to cmake based builds
- updated chlog
* Thu Mar  7 2013 @44857b2
- Merge branch '2.0' of tizen:profile/ivi/libwebsockets into 2.0
- pkgconfig install
- updated spec fixed pkgconfig
- updated spec enabled ssl
- updated spec
- updated spec
- fix win32helpers gettimeofday epoch
- trace 22 fix zero length close from client
- cmake mingw no need for websock w32
- normalize formatting in gettimeofday
- fix win32 gettimeofday for mingw
- cmake lib lib64 problem
- fix mime type on leaf header
- reflect send completeness in lws_write return
- move ssl cipher list from compiletime to context creation time option
- remove MAX_HEADER_NAME_LENGTH from header
- Fix running test programs from within visual studio.
- Print SSL error codes as well as the string.
- Set the _DEBUG macro for CMake also.
- Fixed ssl cert generation on Windows.
- Added CPack support + some more.
- BUGFIX: Fixed bug for installing test-apps for CMake.
- Fixed CMake compile options.
- getifaddrs missing more user friendly in CMake.
- Fix LWS_NO_SERVER build.
- Bugfix compiling for cross compiling.
- keepalive swap interval and probes
- provide socketfd at in param for LWS_CALLBACK_FILTER_NETWORK_CONNECTION
- trac 18 deal with service connection timing out
- cmake fix for older cmake
- update missed extpoll calls to use correct args for ssl
- cmake docs add note about prefix
- Create the "doc" dir before generating docs.
- Added "make install" support to the CMake project.
- trac 17 update set_log_level api notice
- move cms cmake addition to cmake module paths earlier
- add FindGit.cmake
- document ensure_user_space going private
- remove lws_ensure_user_space from public api change return
- update arm build stats
- trim proxy ads plus hostname stg
- restrict http send buffer to 4096
- fix no extensions build
- migrate client hs and c_port into ah
- minor type optimizations
- remove current_alloc_len
- remove header name buffer
- handle http union transition properly
- test server kill skt with minus 1
- handle any POLLIN before error
- close if we tried to close politely just close next time
- api change deliver socket fd to in param of extpoll callbacks
- problems in lws_handle_POLLOUT_event should just close
- robustness protect and document ensure_user_space
- README.coding add note about closing connections
- add by hand http send example
- create user alloc for http if requested
- introduce LWS_CALLBACK_HTTP_WRITEABLE
- just get hostname into canonical_hostname
- fragge able to send chunks larger than rx buffer
- unstaged server changes
- update 1.21 changelog
- check for default protocol rx buf limit
- update changelog
- fix missing cr from closing log
- update echo to use externsion getting api
- Fixed DLL compilation on Windows for CMake.
- Fixed soname and build shared lib for CMake.
- Added so-version information to the lib.
- disable fstack usage
- echo test app needs different lockfile
- update rpm specfile
- introduce attack script
- security disallow repeated GET
- security harden http parser a bit
- fix another escaape runon
- add cyassl keepalive valgrind minimal mem to changelog
- bump version to 1.2 and soname to 3
- api make close api private only
- api remove hangup_on_client
- update test echo for iface info member namechange
- eliminate snprintf
- fix info struct api docs for iface vs interface
- Fixed compilation on Windows.
- update memory performance info
- fix ssl reject path for freeing header allocation
- fix busted debug format in ssl mode
- fix string escape runon
- fix without server
- style cleanup
- valgrind openssl destroy as far as possible
- valgrind client close in a controlled way on SIGINT
- valgrind eliminate uninitialized warning on close
- valgrind also deallocate rx buf on close when client
- valgrind dont close things directly in the callback
- valgrind client go through context destroy on connection error
- client convert to new headers scheme eliminating mallocs
- valgrind free rx_user_buffer if entered CONNMODE_WS_SERVING
- valgrind introduce protocol init and destroy user callbacks
- valgrind context destroy close all conns properly
- valgrind drop header allocation down http path
- replace per header mallocs with single malloc 3 level struct
- improve static allocation notice
- valgrind free context allocations
- remove extension cruft from struct lws
- use part of service buffer to make response not malloc
- remove minimum frame size for deflate
- stop O2 override
- dont close in user callback wrapper let ancestor do it
- fix error path in file transfer
- throw out lws_websocket_related cruft
- optimize wsi using bitfields and enums to chars
- use context service buffer instead of stack for clent_connect
- use context service buffer instead of stack for clent_connect_2
- use context service buffer instead of stack for create_context
- fix non ssl changes missed from context api change
- use context service buffer instead of stack for lws_client_socket_service
- use context service buffer instead of stack for server_socket_service
- add static stack analysis
- dont try figure out listen_service_fd position if unset
- dont try set per socket keepalive timing on bsds
- fix broken listen socket piggybacking
- introduce keepalive option and make common socket options function
- remove receiving timeout for client
- correct test client to close synchronously with last send
- align max frame for mirror protocol to what the code does
- change context creation params to struct
- handshake bail3 should be bail
- remove fixed rx buffer allow definition per protocol
- account for context in static allocation figure
- remove all PATH_MAX or MAX_PATH
- use context service buf in place of large stack arrays
- remove need for filepath buffer on http file serve
- add static linking exception to LICENSE
- add unchanged lgpl 2.1 in LICENSE
- Fix memory leaks when creating a context.
- Generate the API reference in text format, too.
- Fix two typos.
- changelog header lifecycle
- add autotools bits for cyassl
- unionize header token array
- document header lifecycle change
- headers deleted after websocket established
- leverage TOKEN_SKIPPING better in parser
- simplify parsing complete
- act on fatal parse problems
- remove deprecated vcxproj
- update changelog about cmake
- Added build instructions for CMake.
- add README
- Fixed compilation on NetBSD.
- Cleaned up the CyaSSL linking in the CMake project a bit.
- Fixed windows build.
- Added some minor changes to CMake build file.
- Added support for CyaSSL replacement of OpenSSL.
- Added check for inline keyword availability.
- Fixed build on OSX.
- Fixed linux compilation and added more compile options.
- CMake support + fixed windows build. - Finalized CMake support (tested on windows only so far).   - Uses a generated lws_config.h that is included in   private-libwebsocket to pass defines, only used if CMAKE_BUILD is set.   - Support for SSL on Windows.   - Initial support for CyaSSL replacement of OpenSSL (This has been added     to my older CMake-fork but haven't been tested on this version yet). - Fixed windows build (see below for details). - Fixed at least the 32-bit Debug build for the existing Visual Studio   Project. (Not to keen fixing all the others when we have CMake support   anyway (which can generate much better project files)...) - BUGFIXES:   - handshake.c     - used C99 definition of handshake_0405 function   - libwebsocket.c     - syslog not available on windows, put in ifdefs.     - Fixed previous known crash bug on Windows where WSAPoll in       Ws2_32.dll would not be present, causing the poll function pointer       being set to NULL.     - Uninitialized variable context->listen_service_extraseen would       result in stack overflow because of infinite recursion. Fixed by       initializing in libwebsocket_create_context     - SO_REUSADDR means something different on Windows compared to Unix.     - Setting a socket to nonblocking is done differently on Windows.       (This should probably broken out into a helper function instead)     - lwsl_emit_syslog -> lwsl_emit_stderr on Windows.   - private-libwebsocket.h     - PATH_MAX is not available on Windows, define as MAX_PATH     - Always define LWS_NO_DAEMONIZE on windows.     - Don't define lws_latency as inline that does nothing. inline is not       support by the Microsoft compiler, replaced with an empty define       instead. (It's __inline in MSVC)   - server.c     - Fixed nonblock call on windows   - test-ping.c     - Don't use C99 features (Microsoft compiler does not support it).     - Move non-win32 headers into ifdefs.     - Skip use of sighandler on Windows.   - test-server.c     - ifdef syslog parts on Windows.
- Some more Cmake stuff.
- Started redoing CMake support based on the up to date repos
- improve test server poll loop docs
- add note about MIPS opewrt configure options
- remove one more mention of broadcast callback
- introduce library version plus git hash
- remove stray reference to max broadcast size from readme.build
- additional casts allow test server build as cpp
- update changelog tag chrome 26 firefox 18
- renovate test html
- add changelog v1.0 to v1.1
- bump version to 1.1 and soname to 2
- clean out remaining mentions of deprecated broadcast
- get error from getnameinfo if unable to improve hostname and use hostname
- fixes for without server and without client
- fix unused var if no enable openssl
- introduce test echo
- add info about why we close to more places
- roubustness handle problems in read loop better
- server allow NULL protocol map to protocol 0
- change get_peer_addresses to use context wsi latency
- instrument latency
- introduce lws_latency
- fix docs about protocol version supported
- test server terminate cleanly on ctrl c
- evict all broadcast support
- FreeBSD compatibility
- trac 6 expose libwebsockets read with note about not normally needed
- fix ssl bits outside of ifdef coverage
- force client ssl bio nonblocking
- force ssl rw bios nonblocking
- timeout coverage for ssl accept
- break up ssl accept action
- ensure accept is nonblocking
- autocreate foreign broadcast sockets on broadcast
- trac 5 sa_restorer deprecated
- trac 3 document write and context_user
- trac 4 correct libebsocket_service_fd
- update numbers for minimal build footprint
- more LWS_NO_DAEMONIZE
- use correct LWS_NO_DAEMONIZE on test server
- bind gcc debug generation to_DEBUG
- unionize mutually exclusive wsi members
- key_b64 doesnt need to be in wsi
- avoid PATH_MAX in bss in daemonize
- remove all support for pre v13 protocols
- disable private broadcast sockets if enable no fork config option
- align test server extpoll with library dynamic approach
- document memory efficiency
- log major dynamic allocation info
- zlib not needed if no extensions
- introduce without extensions
- refactor README
- syslog requires format string
- revert zlib update 1.2.7
- make use of lock file
- windows compatibility changes for private libwebsockets
- test server add daemonization flag
- test server use syslog logging
- allow_use_of_lwsl_logging in user code
- helper api:  log through syslog
- logging select some lwsl_info usage to be lwsl_notice
- add lwsl_notice
- expose log level in emit
- change bitfield setting to avoid gcc warnings
- improve frame_is_binary setting
- add lws_confirm_legit_wsi
- refactor and introduce without server configure option
- introdice tracking if frame is binary
- different compiler warning fixes
- add lexical parser for headers
- deprecate x google mux
- solve flowcontrol problems
- check errors on shutdown close
- replace hashtable polltable management
- use simple lookup table for extpoll
- include daemonization file whoops
- portability dont assume size of tv.t_usec
- add disable debug to README configuration options list
- including assert h needed on osx
- just use limits.h directly
- introduce daemonize
- client allow remote server to accept with no protocol set
- move array bounds gcc workaround outside function
- update ping test client and stop exposing payload to extensions
- export lswl_hexdump
- roubustness only return 0 from fd service if handled
- configure without client
- test client remove usleep
- refactor output.c
- refactor migrate client stuff to client.c
- add new context arg to libwebsockets_serve_http_file
- robustness server dont exit server on accept problems
- workaround for some gcc array bounds false positive
- add logo to test file
- update test server html serving callback to use aepd whitelist approach
- add libwebsockets.org logo to share
- optimize http file sending
- listen socket more frequent service
- add empty m4 dir as workaround for autoreconf issue
- allow LWS_SOMAXCONN to be defined at configuretime
- extpoll use hashtable for fd tracking
- allow building just the library not the testapps
- make sure we have PATH_MAX on some linux toolchains (AG modified a bit)
- extpoll break out of loop when set or clear finds fd
- http service break into outer loop states
- merge test server extpoll into test server
- optimize extpoll fd delete
- deal with SSL_ERROR_WANT_ in client connect action
- add longlived option to test client
- logging ensure everyone has a newline
- replace ifdefs around close socket with compatible_close
- ssl client certs fix crash
- absorb README.rst into main README and code
- expose compiletime constants to setting from configure
- renable deflate frame buffer expansion fixing DoS
- fix config enable name for getifaddrs
- introduce getifaddrs for toolchains without it
- audit and make all malloc check for OOM
- logging add timestamp
- logging extend level set api to allow setting emission function
- update README with info on new logging scheme
- allow enabling debug contexts from test apps
- introduce logging api and convert all library output to use it
- compile in xcode, privatize debug macro
- update soname and configure to v1.0
- correct autotools warning
- zlib code add OOM checks remove buffer expansion on rx path
- Avoid leaking a socket when SSL_accept fails.
- Print error string on accept failure.
- Increased MAX_BROADCAST_PAYLOAD to match MAX_USER_RX_BUFFER.
- Added README file with some useful tips for using the library.
- Added support for continuation frames on the server.
- Close connection if LWS_CALLBACK_HTTP returns non-zero.
- Fixed to keep reading data until the SSL internal buffer is empty. Before this fix only 2048 bytes were read, the rest were buffered inside SSL until another message arrived!!!
- Added no-cache headers to client handshake: http://www.ietf.org/mail-archive/web/hybi/current/msg09841.html
- Separate compression levels for server and client, increased the later one to zlib default (6).
- More correct handling of inflate result.
- Fixed crash when HTTP requests method is not GET.
- Check if macro SSL_OP_NO_COMPRESSION is defined before trying to use it.
- Using size_t instead of int for deflate-frame offsets and length.
- Added private macro CIPHERS_LIST_STRING to define ciphers list string.
- When choosing a cipher, use the server's preferences.
- Pass URI length to LWS_CALLBACK_HTTP.
- Disable compression for SSL socket, it is a waste of CPU when using compression extensions.
- Using "SSL_CTX_use_certificate_chain_file" instead of "SSL_CTX_use_certificate_file" to support server certificates signed by intermediaries.
- Better definition of "debug" macro for Win32 builds.
- Use __inline for Win32 builds.
- Avoid checking choked pipe if no extension has more data to write.
- zlib update 1.2.7
- Set listen backlog to SOMAXCONN.
- Fixed operator precedence bug.
- Avoid deflate of small packets.
- Support compressed packets bigger than MAX_USER_RX_BUFFER. (AG adapted style and removed logging stuff)
- Allow extensions when no protocol was specified.
- Added extension "deflate-frame". Using by default instead of "deflate-stream".
- Added support for extensions that only manipulate application data.
- Fixed deflate-stream extension. When the output buffer was exhausted the input buffer was discarded without checking if zlib had actually consumed all the input, now we copy the remaining input data for the next call.
- Added private macro AWAITING_TIMEOUT instead of harcoded value 5.
- Fixed spacing.
- Added context creation parameter for CA certificates file.
- Return NULL if the handshake failed to complete, libwebsocket_service_fd closes and frees the websocket in that case.
- Ignoring linux build files
- Use feature check rather than browser check.
- Changed client handshake to use "Origin" instead of "Sec-WebSocket-Origin" as defined by RFC 6455 when using version 13 of the protocol.
- Fixed compiler warnings on Windows.
- Added new status codes from RFC 6455.
- Fixed compiler warning on Windows.
- required version of autoconf can be lower
- Static variable is now const.
- add context construction option to skip server hostname lookup
- add missing docs for new context user pointer
- libwebsocket_service_fd: EAGAIN is harmless, treat like EINTR
- libwebsocket_context: add userspace pointer for use before wsi creation
- lib/Makefile.am: whitespace fix
- add pkg-config file libwebsockets.pc
- Added test.html favicon.ico to EXTRA_DIST.
- Add missing .h files to sources.
- Add kernel doc to extra_dist.
- always taking an interest in ppid wont hurt
- remove depcomp
- stop being so fragile on socket lifecycle
- use autogen.sh
- changelog update
* Mon Dec  3 2012 tripzero <kevron_m_rees@linux.intel.com> 1.0_branch@2e3587f
- Updating changelog for 2.0alpha
* Wed Sep  5 2012 Rusty Lynch <rusty.lynch@intel.com> 0067a71
- Adding Tizen packaging files
* Wed Aug 22 2012 Rusty Lynch <rusty.lynch@intel.com> 71e5369
- Initial packaging
