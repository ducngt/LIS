class HomeComponent:
    COMPONENT_NAME = "home"
    VERSION = "0.2.0"

    def render(self, assembly_result):
        if assembly_result.get("status") != "success":
            return "<h1>HOME assembly error</h1>"

        identity = assembly_result["data"]["identity"]
        hero = assembly_result["data"]["hero"]

        html = f"""
        <section>

            <header>
                <img
                    src="/{identity["logo_path"]}"
                    alt="{identity["institution_name"]}"
                    width="120"
                >

                <div>
                    <strong>
                        {identity["institution_name"]}
                    </strong>

                    <p>
                        {identity["institution_english_name"]}
                    </p>
                </div>
            </header>

            <main>
                <p>
                    {hero["lis_name"]}
                    - {hero["lis_full_name"]}
                </p>

                <h1>
                    {hero["slogan"]}
                </h1>

                <p>
                    {hero["hero_statement"]}
                </p>

                <a href="{hero["primary_action_target"]}">
                    {hero["primary_action_label"]}
                </a>
            </main>

        </section>
        """

        return html


if __name__ == "__main__":
    print(
        "HomeComponent v0.2.0 is ready. "
        "It expects identity and hero data from HomeAssembly."
    )