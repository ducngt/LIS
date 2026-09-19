class HomeComponent:
    COMPONENT_NAME = "home"
    VERSION = "0.1.0"

    def render(self, assembly_result):
        if assembly_result.get("status") != "success":
            return "<h1>HOME assembly error</h1>"

        hero = assembly_result["data"]["hero"]

        html = f"""
        <section>
            <p>{hero["institution_name"]}</p>

            <h1>
                {hero["lis_name"]}
                - {hero["lis_full_name"]}
            </h1>

            <h2>{hero["slogan"]}</h2>

            <p>
                {hero["hero_statement"]}
            </p>

            <a href="{hero["primary_action_target"]}">
                {hero["primary_action_label"]}
            </a>
        </section>
        """

        return html


if __name__ == "__main__":
    print(
        "HomeComponent is ready. "
        "It expects output from HomeAssembly."
    )