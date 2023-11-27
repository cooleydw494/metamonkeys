Instructions for Generating Python Tests:

1. Test Objectives:
   - Cover expected behavior under normal conditions.
   - Simulate and test error handling.
   - Include edge cases and boundary conditions.

2. Use Mocks and Fixtures:
   - Employ mocks and fixtures from `conftest.py` for external dependencies.
   - Specify any specific mock behavior to simulate.

3. Assertions:
   - Verify return values and side effects.
   - Ensure exceptions are raised as expected under error conditions.

4. Test Readability and Maintainability:
   - Follow Python's PEP 8 style guide.
   - Use descriptive names for each test.

5. Parameterized Testing:
   - If applicable, create parameterized tests for various inputs.

6. Setup and Teardown:
   - Include necessary setup or teardown steps.

7. Test Independence:
   - Ensure each test is independent and can be run on its own.
