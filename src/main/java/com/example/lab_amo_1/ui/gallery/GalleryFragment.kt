package com.example.lab_amo_1.ui.gallery

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.fragment.app.Fragment
import com.example.lab_amo_1.R
import kotlin.math.pow
import kotlin.math.sqrt

class GalleryFragment : Fragment() {

    private lateinit var editTextA: EditText
    private lateinit var editTextB: EditText
    private lateinit var editTextC: EditText
    private lateinit var buttonCalculate: Button
    private lateinit var textResult: TextView

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val root = inflater.inflate(R.layout.fragment_gallery, container, false)
        editTextA = root.findViewById(R.id.editTextA)
        editTextB = root.findViewById(R.id.editTextB)
        editTextC = root.findViewById(R.id.editTextC)
        buttonCalculate = root.findViewById(R.id.buttonCalculate)
        textResult = root.findViewById(R.id.textResult)

        buttonCalculate.setOnClickListener {
            calculateResult()
        }

        return root
    }

    private fun calculateResult() {
        val a = editTextA.text.toString().toDoubleOrNull() ?: return
        val b = editTextB.text.toString().toDoubleOrNull() ?: return
        val c = editTextC.text.toString().toDoubleOrNull()

        val cVisible = a / b > 1
        editTextC.visibility = if (cVisible) View.VISIBLE else View.GONE

        val result: Double = when {
            cVisible && c != null -> {
                (a - b) / (a + b) + sqrt((a - b).pow(2) / c)
            }
            !cVisible -> {
                sqrt((a - b) / (a + b) + sqrt(a.pow(b) / 25))
            }
            else -> {
                return
            }
        }

        textResult.text = "Result: $result"
        textResult.visibility = View.VISIBLE
    }
}
