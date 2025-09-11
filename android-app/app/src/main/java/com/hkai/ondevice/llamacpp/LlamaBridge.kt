
package com.hkai.ondevice.llamacpp

object ModelConfig {
    // You can change defaults here or set via UI/config screen
    var defaultModelPath: String = "models/TinyLlama-1.1B-Chat.Q4_K_M.gguf"
    var useGPU: Boolean = true
}

class LlamaBridge {
    init {
        // Load your native library here once you have it (e.g., System.loadLibrary("llama"))
        // System.loadLibrary("llama_jni")
    }

    external fun jniInit(modelPath: String, gpu: Boolean): Boolean
    external fun jniInfer(prompt: String, maxTokens: Int): String

    fun init(modelPath: String = ModelConfig.defaultModelPath, gpu: Boolean = ModelConfig.useGPU): Boolean {
        // Placeholder: without native lib, return false so UI can show stub state
        return try {
            jniInit(modelPath, gpu)
        } catch (t: Throwable) {
            false
        }
    }

    fun infer(prompt: String, maxTokens: Int = 128): String {
        return try {
            jniInfer(prompt, maxTokens)
        } catch (t: Throwable) {
            "[stub] connect llama.cpp JNI and rebuild"
        }
    }
}
