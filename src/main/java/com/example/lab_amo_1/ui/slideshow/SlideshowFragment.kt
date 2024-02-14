package com.example.lab_amo_1.ui.slideshow

import android.os.Bundle
import android.text.Editable
import android.text.InputFilter
import android.text.Spanned
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.example.lab_amo_1.R
import com.example.lab_amo_1.databinding.FragmentSlideshowBinding

class SlideshowFragment : Fragment() {

    private var _binding: FragmentSlideshowBinding? = null
    private val binding get() = _binding!!

    private lateinit var aValuesEditText: EditText
    private lateinit var bValuesEditText: EditText
    private lateinit var resultTextView: TextView
    private lateinit var calculateButton: Button

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentSlideshowBinding.inflate(inflater, container, false)
        val root: View = binding.root

        aValuesEditText = root.findViewById(R.id.editText_a_values)
        bValuesEditText = root.findViewById(R.id.editText_b_values)
        resultTextView = root.findViewById(R.id.textView_result)
        calculateButton = root.findViewById(R.id.button_calculate)

        // Setting input filters to allow only digits and commas
        val filterDigitsCommas = InputFilter { source, _, _, _, _, _ ->
            if (source.toString().matches("[\\d,]*".toRegex())) {
                null
            } else {
                ""
            }
        }
        aValuesEditText.filters = arrayOf(filterDigitsCommas)
        bValuesEditText.filters = arrayOf(filterDigitsCommas)

        // Setting text change listeners to validate input
        aValuesEditText.addTextChangedListener(createTextWatcher(aValuesEditText))
        bValuesEditText.addTextChangedListener(createTextWatcher(bValuesEditText))

        calculateButton.setOnClickListener {
            calculateResult()
        }

        return root
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun calculateResult() {
        val aValuesInput = aValuesEditText.text.toString()
        val bValuesInput = bValuesEditText.text.toString()

        val aValues = aValuesInput.split(",").map { it.trim().toDoubleOrNull() }
        val bValues = bValuesInput.split(",").map { it.trim().toDoubleOrNull() }

        if (aValues.any { it == null } || bValues.any { it == null }) {
            Toast.makeText(context, "Please enter valid numeric values", Toast.LENGTH_SHORT).show()
            return
        }

        val result = calculateF(aValues.filterNotNull(), bValues.filterNotNull())
        resultTextView.text = "Значення f: $result"
    }

    private fun calculateF(aValues: List<Double>, bValues: List<Double>): Double {
        var result = 1.0
        for (a in aValues) {
            val sumB = bValues.sum()
            result *= a * sumB
        }
        return result
    }

    private fun createTextWatcher(editText: EditText): TextWatcher {
        return object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}

            override fun afterTextChanged(s: Editable?) {
                val text = s.toString()
                if (!text.matches("[\\d,]*".toRegex())) {
                    editText.error = "Please enter only numeric values"
                } else {
                    editText.error = null
                }
            }
        }
    }
}
