# what about types of stimulation and words? Match with first or last consonant?
# new events dictionary for simple key access to different types of events
bands = {'Theta': (4, 8), 'Alpha1': (8, 10), 'Alpha2': (10, 12),
         'Beta1': (12, 16), 'Beta2': (16, 20), 'Beta3': (20, 24)}

event_dict = {'ph/bil/p/cv/true/stim/match': 1, 'ph/bil/p/cv/true/stim/not_match': 2, 'ph/bil/p/cv/false/stim/match': 3,
              'ph/bil/p/cv/false/stim/not_match': 4, 'ph/bil/p/cv/true/no_stim': 5, 'ph/bil/p/cv/false/no_stim': 6,
              'ph/bil/p/vc/true/stim/match': 7, 'ph/bil/p/vc/true/stim/not_match': 8, 'ph/bil/p/vc/false/stim/match': 9,
              'ph/bil/p/vc/false/stim/not_match': 10, 'ph/bil/p/vc/true/no_stim': 11, 'ph/bil/p/vc/false/no_stim': 12,
              'ph/bil/b/cv/true/stim/match': 13, 'ph/bil/b/cv/true/stim/not_match': 14,
              'ph/bil/b/cv/false/stim/match': 15,
              'ph/bil/b/cv/false/stim/not_match': 16, 'ph/bil/b/cv/true/no_stim': 17, 'ph/bil/b/cv/false/no_stim': 18,
              'ph/bil/b/vc/true/stim/match': 19, 'ph/bil/b/vc/true/stim/not_match': 20,
              'ph/bil/b/vc/false/stim/match': 21,
              'ph/bil/b/vc/false/stim/not_match': 22, 'ph/bil/b/vc/true/no_stim': 23, 'ph/bil/b/vc/false/no_stim': 24,
              'ph/den/t/cv/true/stim/match': 25, 'ph/den/t/cv/true/stim/not_match': 26,
              'ph/den/t/cv/false/stim/match': 27,
              'ph/den/t/cv/false/stim/not_match': 28, 'ph/den/t/cv/true/no_stim': 29, 'ph/den/t/cv/false/no_stim': 30,
              'ph/den/t/vc/true/stim/match': 31, 'ph/den/t/vc/true/stim/not_match': 32,
              'ph/den/t/vc/false/stim/match': 33,
              'ph/den/t/vc/false/stim/not_match': 34, 'ph/den/t/vc/true/no_stim': 35, 'ph/den/t/vc/false/no_stim': 36,
              'ph/den/d/cv/true/stim/match': 37, 'ph/den/d/cv/true/stim/not_match': 38,
              'ph/den/d/cv/false/stim/match': 39,
              'ph/den/d/cv/false/stim/not_match': 40, 'ph/den/d/cv/true/no_stim': 41, 'ph/den/d/cv/false/no_stim': 42,
              'ph/den/d/vc/true/stim/match': 43, 'ph/den/d/vc/true/stim/not_match': 44,
              'ph/den/d/vc/false/stim/match': 45,
              'ph/den/d/vc/false/stim/not_match': 46, 'ph/den/d/vc/true/no_stim': 47, 'ph/den/d/vc/false/no_stim': 48,
              'wrd/sense/stim': 49, 'wrd/no_sense/stim': 50, 'wrd/sense/no_stim': 51, 'wrd/no_sense/no_stim': 52}
