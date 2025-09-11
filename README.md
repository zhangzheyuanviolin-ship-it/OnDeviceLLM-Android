# On-Device Chat & Translate on Android (Qualcomm GENIE, MLC, WebLLM): Your Phone, Your LLM

This repository contains a **multi-path starter** for building an **offline** Android Chat + Translate app using:

- **Path A (Native + GPU/NPU)**: `android-app/` — Kotlin app with JNI hooks designed for **llama.cpp** (Adreno **OpenCL** backend) and room to add NNAPI/NPU offload.
- **Path B (Compiler stack)**: `mlc-android/` — notes & scaffolding for **MLC-LLM** (TVM-compiled) Android builds.
- **Path C (Web fallback)**: `webllm-pwa/` — a **WebLLM/WebGPU** PWA fallback you can host or side-load as a TWA.

> ⚠️ **Note:** We do not bundle model weights. Use GGUF models (3B–8B recommended) you are licensed to distribute. Place them under `android-app/app/src/main/assets/models/` or use dynamic download.

---

## Quick Start

### Path A — Native Android app (llama.cpp-ready)
1. Open `android-app/` in **Android Studio**.
2. Ensure **NDK** and **CMake** are installed (SDK Manager → SDK Tools).
3. Sync Gradle and run. The app includes a **JNI stub** you will connect to your llama.cpp build.
4. Copy a small **GGUF** model into `app/src/main/assets/models/` (e.g., `TinyLlama-1.1B-Chat.Q4_K_M.gguf`) and update `ModelConfig.kt`.

**Next steps to wire llama.cpp:**
- Add your compiled llama.cpp shared library to `app/src/main/jniLibs/<abi>/` and extend `CMakeLists.txt`.
- Implement JNI bridging in `src/main/cpp/llama_jni.cpp` (tokenize, init, infer).
- Toggle GPU via **OpenCL** (Adreno). Provide runtime flags in `LlamaBridge.kt`.

### Path B — MLC-LLM
- Use `mlc-android/README.md` to clone and build the official MLC Android sample, then copy the generated AAR/binaries here or reference as a submodule.

### Path C — WebLLM PWA
- Serve `webllm-pwa/` locally or deploy as static hosting. On Chrome/Android with **WebGPU**, the demo runs offline once cached.
- Optionally convert into a **Trusted Web Activity** for near-native install.

---

## Benchmarks & Prompts
- Use `benches/run_bench.py` to record latencies across devices and quant levels (Q4_K_M / Q5_K_M / Q8_0). Results saved to CSV.
- Populate `benches/prompts.csv` with your bilingual prompts set.

---

## Project Layout

```
OnDeviceLLM-Android/
  README.md
  LICENSE
  android-app/           # Kotlin + NDK skeleton for llama.cpp (OpenCL-ready placeholders)
  mlc-android/           # MLC-LLM Android integration notes
  webllm-pwa/            # WebLLM PWA fallback
  benches/               # benchmark harness and prompts
  scripts/               # helper scripts (GGUF packaging, ADB install, etc.)
  model-packs/           # manifest schemas for model bundles
```

---

## License
This project is released under the **MIT License**. See `LICENSE` for details.
