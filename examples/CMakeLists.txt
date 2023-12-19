build_lib_example(
  NAME rtc-example
  SOURCE_FILES rtc-test.cc
  LIBRARIES_TO_LINK
    ${libns3-sparkrtc}
    ${libapplications}
    ${libpoint-to-point}
    ${libinternet}
    ${libnetwork}
)
