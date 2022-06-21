import state from '../../../state';
import execute from '../../../execute';
import ServiceResult from '../ServiceResult';
import broadcast from '../../../socket/broadcast';

const containerCreate = (options: any): ServiceResult => {

    if(!state.isConnected) return new ServiceResult(false, 'Not connected to a network');

    if(options.image !== undefined && options.name !== undefined && options.target !== undefined) {

        const command = execute.command.dockerRun(options.image, options.name);

        broadcast.broadcastCommand(command, options.target);

        return new ServiceResult(true, null);

    } else {

        return new ServiceResult(false, 'Wrong option');

    }

};

export default containerCreate;
