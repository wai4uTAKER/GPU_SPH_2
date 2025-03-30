# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import generated.sph_optimized_pb2 as sph__optimized__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in sph_optimized_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class OptimizedSPHSimulationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SimulateStep = channel.unary_unary(
                '/OptimizedSPHSimulation/SimulateStep',
                request_serializer=sph__optimized__pb2.SimulationRequest.SerializeToString,
                response_deserializer=sph__optimized__pb2.SimulationResponse.FromString,
                _registered_method=True)
        self.ExchangeBoundaryParticles = channel.unary_unary(
                '/OptimizedSPHSimulation/ExchangeBoundaryParticles',
                request_serializer=sph__optimized__pb2.BoundaryRequest.SerializeToString,
                response_deserializer=sph__optimized__pb2.BoundaryResponse.FromString,
                _registered_method=True)


class OptimizedSPHSimulationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SimulateStep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExchangeBoundaryParticles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OptimizedSPHSimulationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SimulateStep': grpc.unary_unary_rpc_method_handler(
                    servicer.SimulateStep,
                    request_deserializer=sph__optimized__pb2.SimulationRequest.FromString,
                    response_serializer=sph__optimized__pb2.SimulationResponse.SerializeToString,
            ),
            'ExchangeBoundaryParticles': grpc.unary_unary_rpc_method_handler(
                    servicer.ExchangeBoundaryParticles,
                    request_deserializer=sph__optimized__pb2.BoundaryRequest.FromString,
                    response_serializer=sph__optimized__pb2.BoundaryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OptimizedSPHSimulation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('OptimizedSPHSimulation', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OptimizedSPHSimulation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SimulateStep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/OptimizedSPHSimulation/SimulateStep',
            sph__optimized__pb2.SimulationRequest.SerializeToString,
            sph__optimized__pb2.SimulationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ExchangeBoundaryParticles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/OptimizedSPHSimulation/ExchangeBoundaryParticles',
            sph__optimized__pb2.BoundaryRequest.SerializeToString,
            sph__optimized__pb2.BoundaryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
