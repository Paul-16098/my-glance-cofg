import dotenv
import os


def main(
    # glance args
    args: tuple[str, ...] = (
        # print true cofg
        "config:print>glance.t.yml",
        # diagnose web
        # "diagnose",
        # test env
        "config:validate",
        # run
        "",
    ),
):
    """run and test glance

    :param args: glance args
    :type args: tuple[str, ...]"""
    dotenv.load_dotenv()

    for arg in args:
        try:
            os.system(f"{os.path.join(os.path.dirname(__file__), 'glance')} {arg}")
        except KeyboardInterrupt:
            if arg == "":
                # run
                print("\r---- reload ----")
                main(("",))
            else:
                # not run
                print("\r---- abort ----")
                return


if __name__ == "__main__":
    main()
