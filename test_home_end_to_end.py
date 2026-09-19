from assemblies.home_assembly.assembly import HomeAssembly
from components.home.component import HomeComponent


def main():
    assembly = HomeAssembly()
    component = HomeComponent()

    assembly_result = assembly.execute()

    html = component.render(assembly_result)

    print(html)


if __name__ == "__main__":
    main()