
# Minimal CMake stub. Extend to link your compiled llama.cpp library.
cmake_minimum_required(VERSION 3.22.1)
project(llama_jni)

add_library(llama_jni SHARED llama_jni.cpp)

find_library(log-lib log)

# Example: link against your llama shared lib once added
# add_library(llama SHARED IMPORTED)
# set_target_properties(llama PROPERTIES IMPORTED_LOCATION
#     ${CMAKE_SOURCE_DIR}/../jniLibs/arm64-v8a/libllama.so)

target_link_libraries(llama_jni ${log-lib})
