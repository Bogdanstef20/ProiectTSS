import matplotlib.pyplot as plt
import coverage
import unittest
import os

# Configurare pentru generarea raportului de acoperire
cov = coverage.Coverage()
cov.start()

# Rulează testele
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.discover('.', pattern='test_*.py'))

runner = unittest.TextTestRunner()
runner.run(suite)

cov.stop()
cov.save()

# Generare raport
report = cov.get_data()
files = cov.get_data().measured_files()
report_values = {filename: cov.analysis(filename) for filename in files}

# Calcularea procentului de acoperire
coverage_percentages = {}
for filename, analysis in report_values.items():
    total_lines = len(analysis[0])
    executed_lines = len(analysis[1])
    coverage_percentages[os.path.basename(filename)] = (executed_lines / total_lines) * 100 if total_lines > 0 else 0

# Generare grafic
plt.figure(figsize=(12, 6))  # A crescut dimensiunea figurii pentru a încăpea etichetele
plt.bar(coverage_percentages.keys(), coverage_percentages.values())
plt.xlabel('Modules')
plt.ylabel('Coverage (%)')
plt.title('Test Coverage Report')
plt.xticks(rotation=45, ha='right')  # Rotește etichetele pentru a fi mai lizibile
plt.tight_layout()
plt.savefig('coverage_report.png')
plt.show()
