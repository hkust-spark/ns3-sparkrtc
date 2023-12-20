build_lib_example(
  NAME rtc-test
  SOURCE_FILES rtc-test.cc
  LIBRARIES_TO_LINK
    ${libsparkrtc}
    ${libapplications}
    ${libpoint-to-point}
    ${libinternet}
    ${libnetwork}
)
