from .exporter import Exporter

class ObjectExporter(Exporter):
    def get_blur_matrices(self):
        motion_steps = numpy.linspace(
            self.cache.scene["shutter_start"],
            self.cache.scene["shutter_end"],
            self.cache.scene["motion_keys"]
        )

        marray = ArnoldArray()
        marray.allocate(1, self.cache.scene["motion_keys"], 'MATRIX')

        for i in range(0, motion_steps.size):
            frame, subframe = self.get_target_frame(motion_steps[i])
            self.cache.frame_set(frame, subframe=subframe)

            m = export_utils.flatten_matrix(self.ob.matrix_world)
            marray.set_matrix(i, m)
        
        self.cache.frame_set(self.cache.scene["frame_current"], subframe=0)

        return marray
    
    def get_target_frame(self, motion_step):
        frame_current = self.cache.scene["frame_current"]

        frame_flt = frame_current + motion_step
        frame_int = math.floor(frame_flt)
        subframe = frame_flt - frame_int

        return frame_int, subframe