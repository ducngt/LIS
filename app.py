from flask import Flask

from assemblies.home_assembly.assembly import HomeAssembly
from components.home.component import HomeComponent


app = Flask(__name__)


@app.route("/")
def home():
    assembly = HomeAssembly()
    component = HomeComponent()

    assembly_result = assembly.execute()
    html = component.render(assembly_result)

    return html


if __name__ == "__main__":
    app.run(debug=True)