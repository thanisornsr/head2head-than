# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FacesoftFlatbuffersSchema

import flatbuffers

class SerializedTriMesh(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSerializedTriMesh(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SerializedTriMesh()
        x.Init(buf, n + offset)
        return x

    # SerializedTriMesh
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SerializedTriMesh
    def Points(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SerializedTriMesh
    def PointsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # SerializedTriMesh
    def PointsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SerializedTriMesh
    def TriIndices(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SerializedTriMesh
    def TriIndicesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # SerializedTriMesh
    def TriIndicesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SerializedTriMesh
    def UV(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SerializedTriMesh
    def UVAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # SerializedTriMesh
    def UVLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SerializedTriMesh
    def SubmeshIndexOffset(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # SerializedTriMesh
    def SubmeshIndexOffsetAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # SerializedTriMesh
    def SubmeshIndexOffsetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def SerializedTriMeshStart(builder): builder.StartObject(4)
def SerializedTriMeshAddPoints(builder, Points): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Points), 0)
def SerializedTriMeshStartPointsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SerializedTriMeshAddTriIndices(builder, TriIndices): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(TriIndices), 0)
def SerializedTriMeshStartTriIndicesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SerializedTriMeshAddUV(builder, UV): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(UV), 0)
def SerializedTriMeshStartUVVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SerializedTriMeshAddSubmeshIndexOffset(builder, SubmeshIndexOffset): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SubmeshIndexOffset), 0)
def SerializedTriMeshStartSubmeshIndexOffsetVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SerializedTriMeshEnd(builder): return builder.EndObject()
