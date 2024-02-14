package com.example.lab_amo_1.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.fragment.app.Fragment
import com.example.lab_amo_1.databinding.FragmentHomeBinding
import kotlin.math.cos
import kotlin.math.pow
import kotlin.math.sin

class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!


    private lateinit var editTextA: EditText
    private lateinit var editTextB: EditText
    private lateinit var buttonCalculate: Button
    private lateinit var textViewResult: TextView

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        val root: View = binding.root

        editTextA = binding.editTextA
        editTextB = binding.editTextB
        buttonCalculate = binding.buttonCalculate
        textViewResult = binding.textViewResult

        buttonCalculate.setOnClickListener {
            val a = editTextA.text.toString().toDoubleOrNull()
            val b = editTextB.text.toString().toDoubleOrNull()

            if (a != null && b != null) {
                val result = solveEquation(a, b)
                textViewResult.text = "Y1 = $result"
            } else {
                textViewResult.text = "Please enter valid numbers for a and b."
            }
        }

        return root
    }

    private fun solveEquation(a: Double, b: Double): Double {
        val result = sin(a + b).pow(2) + cos(a - b).pow(2)
        return result
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
