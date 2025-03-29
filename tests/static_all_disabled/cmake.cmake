# CMake include file

# Add more sources
target_sources(${CMAKE_PROJECT_NAME} PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/../test_file.c
)

# LwPKT options
set(LWPKT_OPTS_FILE ${CMAKE_CURRENT_LIST_DIR}/lwpkt_opts.h)