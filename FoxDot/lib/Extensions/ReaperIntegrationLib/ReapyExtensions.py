from reapy import *


# Source of that procedure : https://forum.cockos.com/showthread.php?t=256152 : LUA "add fx chain" is inserting to first slot instead of last
# inspired by MPL script

def move_fx(src_track, dest_track):
    fx_count =  RPR.TrackFX_GetCount(src_track)
    for src_fx in range(fx_count):
        fx_to_move_index = 0 # always move the first fx left on the track
        RPR.TrackFX_CopyToTrack(src_track, fx_to_move_index, dest_track, RPR.TrackFX_GetCount(dest_track), True)

def add_chunk_to_track(track, chunk):  # add empty fx chain chunk if not exists
    track_xml_chunk = RPR.GetTrackStateChunk(track, '', 999999, False)[2]
    #chunk_ch = track_chunk[2]
    if 'FXCHAIN' not in track_xml_chunk:
        track_xml_chunk = track_xml_chunk[0:-3] + '\n<FXCHAIN\nSHOW 0\nLASTSEL 0\n DOCKED 0\n>\n>\n'
    if chunk:
        track_xml_chunk = track_xml_chunk.replace('DOCKED 0', 'DOCKED 0\n ' + chunk)
    RPR.SetTrackStateChunk(track, track_xml_chunk, False)


def add_fx_chain(track, chain_name):
    track = track.id
    fxchain_filepath = RPR.GetResourcePath() + '/FXChains/' + f'{chain_name}.RfxChain'

    if RPR.file_exists(fxchain_filepath):
        with open(fxchain_filepath, "r") as f:
            content = f.read()

    RPR.PreventUIRefresh(1)
    RPR.InsertTrackAtIndex(RPR.CountTracks(0), False)
    last_track = RPR.GetTrack(0,RPR.CountTracks(0)-1)

    add_chunk_to_track(last_track, content)

    move_fx(last_track, track)
    RPR.DeleteTrack(last_track)
    RPR.PreventUIRefresh(-1)

pproject = Project()

#track = pproject.tracks["chan1"]

#add_fx_chain(track, "darkpass")