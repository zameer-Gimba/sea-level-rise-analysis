# tests/test_sea_level_predictor.py
import unittest
import matplotlib.pyplot as plt
import os
import sys

# Add src folder to path if running tests from repo root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import sea_level_predictor


class SeaLevelTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run draw_plot once for all tests to save time."""
        cls.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        """Check if the plot title is correct."""
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_plot_labels(self):
        """Check if x and y labels are correct."""
        self.assertEqual(self.ax.get_xlabel(), "Year")
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_regression_lines_count(self):
        """Check that there are exactly 2 regression lines plotted."""
        # Only lines from plt.plot(), scatter points are not included in ax.get_lines()
        lines = self.ax.get_lines()
        self.assertEqual(len(lines), 2, "There should be exactly 2 regression lines plotted.")

    def test_regression_lines_extent(self):
        """Check that regression lines extend to year 2049 (2050 excluded)."""
        for line in self.ax.get_lines():
            x_data = line.get_xdata()
            self.assertEqual(max(x_data), 2049, "Regression lines should extend to year 2049 (range ends at 2049).")

    def test_plot_file_saved(self):
        """Check that the plot image file was created."""
        self.assertTrue(os.path.exists('sea_level_plot.png'), "File 'sea_level_plot.png' does not exist.")

    @classmethod
    def tearDownClass(cls):
        """Close all plots after tests."""
        plt.close('all')


if __name__ == "__main__":
    unittest.main()
