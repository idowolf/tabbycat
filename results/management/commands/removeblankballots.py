from utils.management.base import TournamentCommand, CommandError
from ...models import BallotSubmission, SpeakerScoreByAdj

class Command(TournamentCommand):

    help = "Removes all blank ballot submissions, i.e. ones without any scores attached."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument("--dry-run", action="store_true")

    def handle_tournament(self, tournament, **options):
        for bsub in BallotSubmission.objects.filter(debate__round__tournament=tournament):
            if not SpeakerScoreByAdj.objects.filter(ballot_submission=bsub).exists():
                if not args.dry_run:
                    self.stdout.write("Deleting {:s}".format(bsub))
                    bsub.delete()
                else:
                    self.stdout.write("Would delete {:s}".format(bsub))