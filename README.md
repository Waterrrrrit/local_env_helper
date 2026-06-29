# local_env_helper
An AI-powered diagnostic tool that analyzes local Python environments and source code to predict and resolve environment-specific errors using the Gemini API.

**<Overview>**
local_env_helper is a Python script designed to detect and troubleshoot environment-dependent issues before code execution. By combining local environment data (OS, paths, dependencies, encodings) with the target source code, it utilizes the Google Gemini API to forecast potential runtime errors and provide specific solutions.

**<Key Features>**

**Environment Profiling**: Extracts and summarizes system information, Python interpreter details, environment variables, and installed packages.

**AI-Driven Analysis**: Evaluates the target Python code against the extracted environment context using the latest google-genai SDK.

**Error Prediction**: Identifies missing modules, version conflicts, encoding issues, and OS-specific limitations.

**Actionable Solution**s: Generates troubleshooting steps tailored to the specific local development setup.

**<Prerequisites>**
Python 3.x

google-genai library

Google Gemini API Key
