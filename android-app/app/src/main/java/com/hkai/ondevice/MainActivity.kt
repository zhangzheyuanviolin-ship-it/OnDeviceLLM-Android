
package com.hkai.ondevice

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.hkai.ondevice.databinding.ActivityMainBinding
import com.hkai.ondevice.llamacpp.LlamaBridge

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val llama = LlamaBridge()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Example init; adjust to your actual model path
        val model = "models/TinyLlama-1.1B-Chat.Q4_K_M.gguf"
        val ok = llama.init(modelPath = model, gpu = true)

        binding.status.text = if (ok) "Model initialized" else "Init failed (stub)"

        binding.send.setOnClickListener {
            val prompt = binding.input.text.toString().trim()
            if (prompt.isNotEmpty()) {
                val out = llama.infer(prompt, maxTokens = 128)
                val prev = binding.transcript.text.toString()
                binding.transcript.text = prev + "\n\n> " + prompt + "\n" + out
                binding.input.setText("")
            }
        }
    }
}
