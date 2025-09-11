
#include <jni.h>
#include <string>

extern "C" JNIEXPORT jboolean JNICALL
Java_com_hkai_ondevice_llamacpp_LlamaBridge_jniInit(
    JNIEnv* env, jobject /*thiz*/, jstring modelPath, jboolean gpu
) {
    // TODO: Initialize llama.cpp runtime and load model
    // Use OpenCL/Vulkan flags as needed
    return JNI_TRUE; // return false until wired
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_hkai_ondevice_llamacpp_LlamaBridge_jniInfer(
    JNIEnv* env, jobject /*thiz*/, jstring prompt, jint maxTokens
) {
    // TODO: Call into llama.cpp to run inference and stream tokens
    const char* p = env->GetStringUTFChars(prompt, 0);
    std::string out = std::string("[stub] You said: ") + p;
    env->ReleaseStringUTFChars(prompt, p);
    return env->NewStringUTF(out.c_str());
}
