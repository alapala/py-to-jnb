import io
import nbformat as nbf
import py2nb
import unittest


class ExampleCodeFiles(unittest.TestCase):
    def test_code_without_cells(self):
        code = r'''
import numpy as np

# Data from text
x = np.array([
    [2.253, 4.485],
    [2.277, 4.526]
]).T
v = np.exp(x)
'''.lstrip()
        expected_result = r'''
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Data from text\n",
    "x = np.array([\n",
    "    [2.253, 4.485],\n",
    "    [2.277, 4.526]\n",
    "]).T\n",
    "v = np.exp(x)"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
'''.lstrip()

        codestream = io.StringIO(code)
        nb = py2nb.notebook_cell_parse(codestream)

        outputstream = io.StringIO()
        nbf.write(nb, outputstream)

        self.assertEqual(outputstream.getvalue(), expected_result)

    def test_code_with_cells(self):
        code = r'''
import numpy as np

# Data from text
x = np.array([
    [2.253, 4.485],
    [2.277, 4.526]
]).T

# Derive values ----

v = np.exp(x)
'''.lstrip()
        expected_result = r'''
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Data from text\n",
    "x = np.array([\n",
    "    [2.253, 4.485],\n",
    "    [2.277, 4.526]\n",
    "]).T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Derive values ----\n",
    "\n",
    "v = np.exp(x)"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
'''.lstrip()

        codestream = io.StringIO(code)
        nb = py2nb.notebook_cell_parse(codestream)

        outputstream = io.StringIO()
        nbf.write(nb, outputstream)

        self.assertEqual(outputstream.getvalue(), expected_result)


if __name__ == '__main__':
    unittest.main()
