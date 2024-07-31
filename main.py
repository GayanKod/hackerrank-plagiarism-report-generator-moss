import sys
import mosspy
import os
import weasyprint
import re


USER_ID = 397744869


class Job:

    def _generate_job_name(self):
        main_path, base_dir_name = os.path.split(self.base_dir)
        return f"Coderush2022-{base_dir_name}-{self.lang}"

    def __init__(self, lang, base_dir):
        self.dirs = []
        self.moss = mosspy.Moss(USER_ID, lang)
        self.lang = lang
        self.base_dir = base_dir
        self.url = None
        self.job_name = self._generate_job_name()

    def add_dir(self, dir_name):
        full_path = os.path.join(self.base_dir, dir_name, "*")
        self.dirs.append(full_path)
        self.moss.addFilesByWildcard(full_path)

    def upload(self):
        url = self.moss.send(
            lambda filepath, display_name: print("Uploading...", display_name))
        self.url = url
        return url

    def __str__(self):
        return f"<JOB:{self.job_name}>"


# generate job list for given question
def generate_job_list(dir_path):
    jobs = {}
    for lang_dir in os.listdir(dir_path):
        if re.match("^py", lang_dir):
            name = "python"
        elif re.match("javascript", lang_dir):
            name = "javascript"
        elif re.match("^java", lang_dir):
            name = "java"
        elif re.match("^c$", lang_dir):
            name = "c"
        elif re.match("cpp", lang_dir):
            name = "cc"
        elif re.match("ada", lang_dir):
            name = "ada"
        else:
            print("unknown language,", lang_dir)
            continue

        # Update job
        if name not in jobs:
            jobs[name] = Job(name, dir_path)
        jobs[name].add_dir(lang_dir)
    return jobs


def log_to_file(question_path, lines):
    with open(os.path.join(question_path, 'reports.txt'), 'w') as file:
        file.writelines(lines)


if len(sys.argv) < 2:
    print("Invalid arguments")
    exit(1)


def main(questions):
    for q in questions:
        log_lines = []
        if input(f"Are you want to check for {q}: ") != "y":
            continue
        print("Performing", q)
        question_path = os.path.join(cwd, q)
        job_list = generate_job_list(question_path)
        for job_k in job_list:
            job = job_list.get(job_k)
            print("Job,", q, job.job_name)
            url = job.upload()
            print("Done,", url)
            log_lines.append(f"{job.job_name} {url}\n")
            weasyprint.HTML(url=url).write_pdf(
                os.path.join(question_path, f"{job.job_name}.pdf"))
            print("PDF Report saved")
        log_to_file(question_path, log_lines)
        print("Quesion done")
        input()


if __name__ == '__main__':
    cwd = sys.argv[1]
    questions = os.listdir(cwd)
    main(questions)

