import dotenv
import os

RUN_ARG = ">glance.log"


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
        RUN_ARG,
    ),
):
    """run and test glance

    :param args: glance args
    :type args: tuple[str, ...]"""
    dotenv.load_dotenv()

    for arg in args:
        try:
            os.system(f"cd {os.path.abspath(os.path.dirname(__file__))}&glance {arg}")
        except KeyboardInterrupt:
            if arg == RUN_ARG:
                # run
                print("\r---- reload ----")
                main((RUN_ARG,))
            else:
                # not run
                print("\r---- abort ----")
                return


if __name__ == "__main__":
    main()
