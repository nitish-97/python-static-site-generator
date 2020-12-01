import typer
import Site from ssg.site

# def if __name__ == "__main__":
#     pass

def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }
    Site(**config).build()

typer.run(main)
