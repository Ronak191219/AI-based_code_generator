from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/", methods=["GET", "POST"])
def index():

    generated_code = ""

    if request.method == "POST":

        prompt = request.form["prompt"]

        try:

            response = model.generate_content(
    f"""
You are an expert AI Code Generator.

Rules:
1. Generate ONLY the requested code.
2. Do NOT include explanations before or after the code.
3. Keep the code concise and professional.
4. Add comments only when necessary.
5. If the user asks for a complete project, generate the complete project code.
6. If the programming language is not mentioned, use Python by default.
7. Return plain code only (no markdown, no ```).

User Request:
{prompt}
"""
)
            generated_code = (
                response.text
                .replace("```python", "")
                .replace("```java", "")
                .replace("```cpp", "")
                .replace("```c++", "")
                .replace("```javascript", "")
                .replace("```js", "")
                .replace("```html", "")
                .replace("```css", "")
                .replace("```sql", "")
                .replace("```c", "")
                .replace("```csharp", "")
                .replace("```cs", "")
                .replace("```php", "")
                .replace("```go", "")
                .replace("```swift", "")
                .replace("```kotlin", "")
                .replace("```ruby", "")
                .replace("```r", "")
                .replace("```", "")
                .strip()
            )

        except Exception as e:
            print("Error:", e)
            generated_code = f"⚠️ Error: {str(e)}"

    return render_template("index.html", code=generated_code)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))