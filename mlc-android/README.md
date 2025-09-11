# MLC-LLM Android Integration

This folder documents how to bring an **MLC-LLM** build into the main Android app.

## Steps
1. Follow MLC-LLM Android build docs to compile the runtime and a chosen model.
2. Export the generated AAR or `.so` artifacts.
3. Create a new Android module here, add the AAR as a dependency, and expose a thin Kotlin wrapper `MlcllmBridge.kt` with the same `init()`/`infer()` shape as `LlamaBridge`.
4. In the main app, add a settings toggle to switch between **llama.cpp** and **MLC** at runtime.
5. Keep a compatibility layer interface (e.g., `EngineBridge`) so either backend can be hot-swapped.
